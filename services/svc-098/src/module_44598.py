"""Service module 44598: business logic, no crypto."""


def calculate_total_44598(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44598():
    return 'module 44598 handles orders and invoices'
