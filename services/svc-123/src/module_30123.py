"""Service module 30123: business logic, no crypto."""


def calculate_total_30123(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30123():
    return 'module 30123 handles orders and invoices'
