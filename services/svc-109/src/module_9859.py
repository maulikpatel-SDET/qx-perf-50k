"""Service module 9859: business logic, no crypto."""


def calculate_total_9859(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9859():
    return 'module 9859 handles orders and invoices'
