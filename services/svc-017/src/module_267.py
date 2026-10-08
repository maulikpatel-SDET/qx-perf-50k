"""Service module 267: business logic, no crypto."""


def calculate_total_267(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_267():
    return 'module 267 handles orders and invoices'
