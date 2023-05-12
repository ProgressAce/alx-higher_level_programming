#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to the head of the list.
 * @number: the number to insert.
 *
 * Return: address of new node, or NULL if failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *prev = NULL, *new = NULL;
	int x = 0;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (current == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}

	while (current)
	{
		if (current->n >= number)
		{
			new->next = current;
			if (x != 0) /* first node doesn't have previous node */
				prev->next = new;
			else
				*head = new;

			return (new);
		}
		if (x > 0)
			prev = current;
		if (current->next == NULL)
		{
			new->next = NULL;
			current->next = new;
			return (new);
		}
		x++;
		current = current->next;
	}
	return (NULL);
}
