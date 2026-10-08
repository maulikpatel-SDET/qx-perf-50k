"""Service module 46583: business logic, no crypto."""


def calculate_total_46583(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46583():
    return 'module 46583 handles orders and invoices'
