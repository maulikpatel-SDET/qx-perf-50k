"""Service module 14978: business logic, no crypto."""


def calculate_total_14978(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14978():
    return 'module 14978 handles orders and invoices'
