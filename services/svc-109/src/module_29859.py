"""Service module 29859: business logic, no crypto."""


def calculate_total_29859(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29859():
    return 'module 29859 handles orders and invoices'
