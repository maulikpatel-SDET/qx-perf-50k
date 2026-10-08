"""Service module 27823: business logic, no crypto."""


def calculate_total_27823(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27823():
    return 'module 27823 handles orders and invoices'
