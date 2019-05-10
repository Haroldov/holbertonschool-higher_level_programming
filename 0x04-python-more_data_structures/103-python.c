#include <Python.h>
#include <stdio.h>
#include <string.h>
void print_python_bytes(PyObject *p);

/**
 *print_python_list - print some basic info about Python lists
 *@p: python object
 *Return: none
 */

void print_python_list(PyObject *p)
{
	unsigned int i = 0;
	const char *str = NULL;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", ((PyVarObject *)p)->ob_size);
	printf("[*] Allocated = %li\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < ((PyVarObject *)p)->ob_size; i++)
	{
		str = ((PyListObject *)p)->ob_item[i]->ob_type->tp_name;
		printf("Element %i: %s\n", i, str);
		if (strcmp(str, "bytes") == 0)
			print_python_bytes(((PyListObject *)p)->ob_item[i]);
	}
}

/**
 *print_python_bytes - print some basic info about Python bytes
 *@p: python object
 *Return: none
 */

void print_python_bytes(PyObject *p)
{
	unsigned int bytes, i = 0;
	char *str = ((PyBytesObject *)p)->ob_sval;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		printf("  size: %li\n", ((PyVarObject *)p)->ob_size);
		printf("  trying string: %s\n", str);
		bytes = ((PyVarObject *)p)->ob_size <= 10 ?
			((PyVarObject *)p)->ob_size + 1 : 10;
		printf("  first %i bytes:", bytes);
		for (i = 0; i < bytes; i++)
			if (i + 1 >= bytes)
				printf("%02x", str[i] & 0xFF);
			else
				if (i == 0)
					printf(" %02x ", str[i] & 0xFF);
				else
					printf("%02x ", str[i] & 0xFF);
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}
