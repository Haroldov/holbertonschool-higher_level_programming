#include <Python.h>
#include <stdio.h>
#include <locale.h>
/**
 *print_python_string - prints python string
 *@p: pyobject
 *Return: none
 */

void print_python_string(PyObject *p)
{
	setlocale(LC_CTYPE, "");
	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		printf("type: compact ascii\n");
		printf("length: %li\n", ((PyASCIIObject *) p)->length);
		printf("string: %s\n", PyUnicode_AS_DATA(p));
	}
	else if (PyUnicode_IS_COMPACT(p) && !PyUnicode_IS_ASCII(p))
	{
		printf("type: compact unicode object\n");
		printf("length: %li\n", PyUnicode_GET_DATA_SIZE(p) / 4);
		wprintf(L"string: %ls\n", (wchar_t *)_PyUnicode_COMPACT_DATA(p));
		/* printf("%i\n", a); */
	}

}
