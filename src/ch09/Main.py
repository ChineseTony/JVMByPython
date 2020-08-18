#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Main.py
@time: 2019/9/12 9:55
@desc: 主函数
"""
import os
from optparse import OptionParser

from ch09.Cmd import Cmd
from ch09.Interpreter import Interpreter
from ch09.classpath.Classpath import Classpath
from ch09.rtda.heap.ClassLoader import ClassLoader


def main(input_args=None):
    # 设置传入参数
    parser = OptionParser(usage="usage:%prog [-options] class [args...]")

    parser.add_option("-v", "--version", action="store_true", default=False, dest="version_flag",
                      help="print version and exit.")
    parser.add_option("--verbose", action="store_true", default=False, dest="verbose_class_flag",
                      help="enable verbose output")
    parser.add_option("--verbose:class", action="store_true", default=False, dest="verbose_class_flag",
                      help="enable verbose of class loader info output")
    parser.add_option("--verbose:inst", action="store_true", default=False, dest="verbose_inst_flag",
                      help="enable verbose of instruction execute info output")
    parser.add_option("--cp", action="store", type="string", dest="cpOption", help="classpath")
    parser.add_option("--classpath", action="store", type="string", dest="cpOption", help="classpath")
    parser.add_option("--Xjre", action="store", type="string", dest="XjreOption", help="path to jre")
    # 解析参数
    (options, args) = parser.parse_args(input_args)
    if options:
        cmd = Cmd(options, args)

        if not options.version_flag:
            # 启动JVM
            start_JVM(cmd)


# 启动JVM函数
def start_JVM(cmd):
    class_path = Classpath.parse(cmd.XjreOption, cmd.cpOption)
    print("classpath:{0} class:{1} args:{2}".format(class_path, cmd.class_name, cmd.args))

    class_loader = ClassLoader(class_path, cmd.verbose_class_flag)

    class_name = cmd.class_name.replace(".", "/")
    main_class = class_loader.load_class(class_name)
    main_method = main_class.get_main_method()

    if main_method:
        Interpreter.interpret(main_method, cmd.verbose_inst_flag, cmd.args)
    else:
        print("Main method not found in class {0}".format(cmd.class_name))


if __name__ == '__main__':
    Xjre_path = os.path.join(os.environ.get("JAVA_HOME"), "jre")
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    resources_path = os.path.join(os.path.dirname(root_path), "java/class")

    # 1. 执行GetClassTest程序
    # fake_args = ['--Xjre', Xjre_path, '--verbose:inst','--cp', resources_path, 'jvmgo.book.ch09.GetClassTest']
    fake_args = ['--Xjre', Xjre_path, '--cp', resources_path, 'jvmgo.book.ch09.GetClassTest']

    # 2. 执行StringTest程序，执行结果为True, False, True
    # fake_args = ['--Xjre', Xjre_path, '--verbose:inst','--cp', resources_path, 'jvmgo.book.ch09.StringTest']
    # fake_args = ['--Xjre', Xjre_path, '--cp', resources_path, 'jvmgo.book.ch09.StringTest']

    # 3. 执行ObjectTest程序
    # fake_args = ['--Xjre', Xjre_path, '--verbose:inst', '--cp', resources_path, 'jvmgo.book.ch09.ObjectTest']
    # fake_args = ['--Xjre', Xjre_path, '--cp', resources_path, 'jvmgo.book.ch09.ObjectTest']

    # 4. 执行CloneTest程序
    # fake_args = ['--Xjre', Xjre_path, '--verbose:inst', '--cp', resources_path, 'jvmgo.book.ch09.CloneTest']
    # fake_args = ['--Xjre', Xjre_path, '--cp', resources_path, 'jvmgo.book.ch09.CloneTest']

    # 5. 执行BoxTest程序
    # fake_args = ['--Xjre', Xjre_path, '--verbose:inst', '--cp', resources_path, 'jvmgo.book.ch09.BoxTest']
    # fake_args = ['--Xjre', Xjre_path, '--cp', resources_path, 'jvmgo.book.ch09.BoxTest']

    main(fake_args)
