#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 *insert_node - inserts a number into a sorted singly linked list.
 *@head: head of the linked list
 *@number: number to add
 *Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t)), *head_cpy;
	listint_t *tmp;

	if (new_node == NULL || head == NULL || *head == NULL)
		return (NULL);
	head_cpy = *head;
	tmp = *head;
	(*new_node).n = number;
	while (head_cpy != NULL)
	{
		if ((*head_cpy).n > number)
			break;
		else
		{
			tmp = head_cpy;
			head_cpy = (*head_cpy).next;
		}
	}
	if (head_cpy != NULL)
	{
		if (tmp == *head)
		{
			(*new_node).next = tmp;
			*head = new_node;
			return (new_node);
		}
		else
		{
			(*new_node).next = (*tmp).next;
			(*tmp).next = new_node;
			return (new_node);
		}
	}
	return (NULL);
}
