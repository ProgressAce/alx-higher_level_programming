#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to pointer to the head of the listint_t list
 *
 * Return: 0 if list is not a palindrome, or 1 if it is.
 */

int is_palindrome(listint_t **head)
{
	listint_t *current;
	int i, length = 0, middle, part1 = 0, part2 = 0;

	current = *head;
	while(current)
	{
		length++;
		current = current->next;
	}

	/* the centre of the singly linked list */
	middle = length / 2;

	current = *head;
	for(i = 0; current; i++, current = current->next)
	{
		/* if list has odd numer of nodes then ignore the centre one */
		if (i == middle && length % 2 == 1)
			continue;
		else
		{
			if (i < middle)
				part1 += current->n;
			else
				part2 += current->n;
		}
	}

	/* checks if list is palindrome and validates for empty linked list */
	if (part1 == part2)
		return (1);
	else
		return (0);
}
