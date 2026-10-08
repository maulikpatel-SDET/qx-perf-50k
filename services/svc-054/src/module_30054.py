"""Service module 30054: business logic, no crypto."""


def calculate_total_30054(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30054():
    return 'module 30054 handles orders and invoices'
