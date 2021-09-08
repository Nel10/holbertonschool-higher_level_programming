#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - inserting a node
 * @head: head of list
 * @number: number
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nodo;
	listint_t *new_node;

	nodo = *head;
	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (nodo == NULL || nodo->n >= number)
	{
		new_node->next = nodo;
		*head = new_node;
		return (new_node);
	}
	while (nodo && nodo->next && nodo->n < number)
		nodo = nodo->next;
	new_node->next = nodo->next;
	nodo->next = new_node;

	return (new_node);
}
