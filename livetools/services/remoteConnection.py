import os


class RemoteConnection:
    root_folder = '\\\\10.172.235.60\\library02'

    def __init__(self) -> None:
        pass

    def list_folder_server_live_remote_windows_host(self):
        dir_list = os.listdir(f'{self.root_folder}\\Desenvolvimento\\Distribuição\\Practico Live\\Versoes Server')
        new_set = sorted(dir_list, key=lambda folder: str.replace(folder, '.', ''))
        filtered = [x for x in new_set if x[:4].replace('.', '') != '65']
        print(filtered)
        return filtered
