#include "lists.h"
#include <stdio.h>

/**
 *check_cycle - checks if a singly linked list has a cycle in it.
 *@list: pointer to the list
 *Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *hare = list, *turtle = list;

	while (hare != NULL && (*hare).next != NULL)
	{
		hare = hare->next->next;
		turtle = turtle->next;
		if (hare == turtle)
			break;
	}
	if (hare == NULL || (*hare).next == NULL)
		return (0);
	else
		return (1);
}
