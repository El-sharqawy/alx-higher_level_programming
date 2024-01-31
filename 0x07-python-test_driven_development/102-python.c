#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - prints a string informations
 *
 * @py: a Python Object
 *
 * Return: void.
 */
void print_python_string(PyObject *py)
{
	PyObject *str;
	PyObject *repr;

	void(repr);
	printf("[.] string object info\n");

	if (strcmp(py->ob_type->tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(py))
	{
		printf("  type: compact ascii\n");
	}
	else
	{
		printf("  type: compact unicode object\n");
	}

	repr = PyObject_Repr(py);
	str = PyUnicode_AsEncodedString(py, "utf-8", "~E~");
	printf("  length: %ld\n", PyUnicode_GET_SIZE(py));
	printf("  value: %s\n", PyBytes_AsString(str));
}
