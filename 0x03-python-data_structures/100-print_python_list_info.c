#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: Python Object
 */

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyListObject *obj = PyListObject(p);

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", pylist_obj.ob_size);
	for(i = 0; i < obj->ob_size; i++)
	{
		printf("Element %i: &s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
	}
}
