"""Service module 34978: business logic, no crypto."""


def calculate_total_34978(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34978():
    return 'module 34978 handles orders and invoices'
