#include <stdio.h>
#include "lists.h"

/**
 *is_palindrome - checks if a singly linked list is palindrome or not
 *@head: head of the singly linked list
 *Return: 0 if it is not a palindrome, 1 if it is
 */

int is_palindrome(listint_t **head)
{
	listint_t *node = *head, *tmp = NULL, *comp = NULL;

	if (*head == NULL)
		return (1);
	while (node->next != tmp)
	{
		tmp = *head;
		while (tmp->next != comp)
		{
			tmp = tmp->next;
		}
		if (tmp->n != node->n)
			return (0);
		comp = tmp;
		node = node->next;
	}
	return (1);
}
