#include "lists.h"

/**
 * check_cycle - checks if a cycle occurs in a singly linked list.
 * @list: the head of the list.
 *
 * Return: 0 if a cycle has not been found, 1 if it has been found.
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list, *prev_node = NULL;

	while (current)
	{
		 /* points to first node for all prev nodes to be checked */
		prev_node = list;
		while (1)
		{
			if (current->next == prev_node)
				return (1);

			if (prev_node == current)
				break;

			prev_node = prev_node->next;
		}
		current = current->next;
	}

	return (0);
}
