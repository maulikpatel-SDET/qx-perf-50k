"""Service module 18117: business logic, no crypto."""


def calculate_total_18117(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18117():
    return 'module 18117 handles orders and invoices'
