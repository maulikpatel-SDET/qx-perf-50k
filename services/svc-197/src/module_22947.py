"""Service module 22947: business logic, no crypto."""


def calculate_total_22947(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22947():
    return 'module 22947 handles orders and invoices'
