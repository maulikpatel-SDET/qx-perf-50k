"""Service module 36307: business logic, no crypto."""


def calculate_total_36307(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36307():
    return 'module 36307 handles orders and invoices'
