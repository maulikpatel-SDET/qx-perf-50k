"""Service module 34821: business logic, no crypto."""


def calculate_total_34821(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34821():
    return 'module 34821 handles orders and invoices'
