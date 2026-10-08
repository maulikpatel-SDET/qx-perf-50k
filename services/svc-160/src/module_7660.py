"""Service module 7660: business logic, no crypto."""


def calculate_total_7660(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7660():
    return 'module 7660 handles orders and invoices'
