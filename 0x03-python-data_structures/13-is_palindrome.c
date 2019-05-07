#include <stdio.h>
#include "lists.h"

/**
 *is_palindrome - checks if a singly linked list is a palindrome
 *@head: head of the singly linked list
 *Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *node = *head;
	unsigned int len = 0, ind = 0;
	int sum = 0;

	while (node != NULL)
	{
		sum += node->n;
		node = node->next;
		len++;
	}
	if (sum % 2 == 0 && len % 2 == 0)
		return (1);
	if (len % 2 != 0)
	{
		for (ind = 0; ind < len / 2 ; ind++)
			node = node->next;
		sum -= node->n;
		if (sum % 2 == 0)
			return (1);
	}
	return (0);
}
