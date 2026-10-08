"""Service module 27164: business logic, no crypto."""


def calculate_total_27164(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27164():
    return 'module 27164 handles orders and invoices'
