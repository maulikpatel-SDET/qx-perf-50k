"""Service module 4747: business logic, no crypto."""


def calculate_total_4747(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4747():
    return 'module 4747 handles orders and invoices'
