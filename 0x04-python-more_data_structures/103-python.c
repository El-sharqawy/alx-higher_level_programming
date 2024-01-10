#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - print list bytes informations
 *
 * @p: Python Object
 *
 * Return: void.
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int i, limit, size;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	str = ((PyBytesObject *)p)->ob_sval;
	size = ((PyVarObject *)(p))->ob_size;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;
	printf("  first %ld bytes:", limit);
	for (i = 0; i < limit; i++)
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", str[i] + 256);

	printf("\n");
}

/**
 * print_python_list - print Python list informations & Types.
 *
 * @p: Python Object.
 *
 * Return: void.
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyObject *pyObj;
	PyListObject *pyList;

	/* set passed object data */
	pyList = (PyListObject *)p;
	size = ((PyVarObject *)(p))->ob_size;
	printf("[*] Python list info\n");
	printf("[*] Size of the Pyton List = %ld\n", size);
	printf("[*] Allocated = %ld\n", pyList->allocated);
	for (i = 0; i < size; i++)
	{
		pyObj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((pyObj)->ob_type)->tp_name);
		if (PyBytes_Check(pyObj))
		{
			print_python_bytes(pyObj);
		}
	}
}
