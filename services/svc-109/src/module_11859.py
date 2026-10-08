"""Service module 11859: business logic, no crypto."""


def calculate_total_11859(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11859():
    return 'module 11859 handles orders and invoices'
