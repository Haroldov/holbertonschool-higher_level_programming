#include <stdio.h>
#include "lists.h"

/**
 *is_palindrome - checks if a singly linked list is a palindrome
 *@head: head of the singly linked list
 *Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *node = *head, *tmp = *head;
	unsigned int len = 0, i = 0, j = 0;

	while (node != NULL)
	{
		node = node->next;
		len++;
	}
	node = *head;
	while (i < len / 2)
	{
		tmp = *head;
		for (j = 0; j < len - 1; j++)
			tmp = tmp->next;
		if (tmp->n != node->n)
			return (0);
		node = node->next;
		len--;
	}
	return (1);
}
