"""Service module 30747: business logic, no crypto."""


def calculate_total_30747(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30747():
    return 'module 30747 handles orders and invoices'
