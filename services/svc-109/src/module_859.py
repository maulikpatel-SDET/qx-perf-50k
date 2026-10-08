"""Service module 859: business logic, no crypto."""


def calculate_total_859(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_859():
    return 'module 859 handles orders and invoices'
