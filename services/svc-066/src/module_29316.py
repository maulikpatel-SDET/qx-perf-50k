"""Service module 29316: business logic, no crypto."""


def calculate_total_29316(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29316():
    return 'module 29316 handles orders and invoices'
