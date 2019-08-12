class FileController:

    @staticmethod
    def read_file(file_name):
        """
        Read a file
        :param file_name: string (input file)
        :return: file's content: string
        """
        with open(file_name) as file:
            return file.read()

    @staticmethod
    def write_file(data, file_name):
        """
        Write to a file
        :param data: string
        :param file_name: string (output file)
        """
        with open(file_name, 'w') as file:
            file.write(data)
