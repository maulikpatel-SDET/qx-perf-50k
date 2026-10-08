"""Service module 21859: business logic, no crypto."""


def calculate_total_21859(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21859():
    return 'module 21859 handles orders and invoices'
