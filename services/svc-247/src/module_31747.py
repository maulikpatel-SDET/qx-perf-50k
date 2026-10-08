"""Service module 31747: business logic, no crypto."""


def calculate_total_31747(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31747():
    return 'module 31747 handles orders and invoices'
