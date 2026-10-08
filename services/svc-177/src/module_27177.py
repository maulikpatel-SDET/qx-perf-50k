"""Service module 27177: business logic, no crypto."""


def calculate_total_27177(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27177():
    return 'module 27177 handles orders and invoices'
