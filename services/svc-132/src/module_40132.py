"""Service module 40132: business logic, no crypto."""


def calculate_total_40132(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40132():
    return 'module 40132 handles orders and invoices'
