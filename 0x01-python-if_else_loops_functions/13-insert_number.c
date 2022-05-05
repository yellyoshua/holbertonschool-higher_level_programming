#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 *
 * @head: pointer to the head of the list.
 * @number: number to be inserted.
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *newnode = NULL;

	newnode = malloc(sizeof(listint_t));
	if (!newnode)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;
	if (!*head)
	{
		*head = newnode;
		return (newnode);
	}
	if (newnode->n < current->next->n)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	while (current->next && current->next->n < newnode->n)
		current = current->next;
	newnode->next = current->next;
	current->next = newnode;
	return (newnode);
}
