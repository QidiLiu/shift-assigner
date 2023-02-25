# coding: utf-8

'''

<shift-assigner: assign your collegue's shifts automatically>
Copyright (C) <2023> <QidiLiu https://github.com/qidiliu>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''


import tkinter as tk
import tkinter.simpledialog as tk_simpledialog
import utils

if (__name__ == '__main__'):
    root = tk.Tk()
    root.wm_withdraw()
    _person_name = tk_simpledialog.askstring(title='📅', prompt=utils.addSpace('請輸入您的名字：'))
    _test_str = tk_simpledialog.askstring(title='📅', prompt=utils.addSpace('哈哈哈哈：'))
    if _person_name is not None:
        print('Hello, ' + _person_name + '!')
        root.destroy()
    else:
        root.destroy()
    
    root.mainloop()
