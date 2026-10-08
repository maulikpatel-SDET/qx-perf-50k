"""Service module 27308: business logic, no crypto."""


def calculate_total_27308(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27308():
    return 'module 27308 handles orders and invoices'
