"""Service module 2747: business logic, no crypto."""


def calculate_total_2747(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2747():
    return 'module 2747 handles orders and invoices'
