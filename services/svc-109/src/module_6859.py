"""Service module 6859: business logic, no crypto."""


def calculate_total_6859(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6859():
    return 'module 6859 handles orders and invoices'
