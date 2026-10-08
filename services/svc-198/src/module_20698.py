"""Service module 20698: business logic, no crypto."""


def calculate_total_20698(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20698():
    return 'module 20698 handles orders and invoices'
