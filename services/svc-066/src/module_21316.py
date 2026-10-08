"""Service module 21316: business logic, no crypto."""


def calculate_total_21316(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21316():
    return 'module 21316 handles orders and invoices'
