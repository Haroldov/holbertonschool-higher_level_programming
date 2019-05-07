#include <stdio.h>
#include "lists.h"

/**
 *is_palindrome - checks if a singly linked list is palindrome or not
 *@head: head of the singly linked list
 *Return: 0 if it is not a palindrome, 1 if it is
 */

int is_palindrome(listint_t **head)
{
	listint_t *node = *head;
	unsigned int len = 0, ind = 0;
	int sum = 0, halfSum = 0;

	if (*head == NULL)
		return (1);
	while (node != NULL)
	{
		sum += node->n;
		node = node->next;
		len++;
	}
	node = *head;
	for (ind = 0; ind < len / 2 ; ind++)
	{
		halfSum += node->n;
		node = node->next;
	}
	if (len % 2 != 0)
		sum -= node->n;
	if (sum / 2 == halfSum)
		return (1);
	return (0);
}
