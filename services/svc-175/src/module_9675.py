"""Service module 9675: business logic, no crypto."""


def calculate_total_9675(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9675():
    return 'module 9675 handles orders and invoices'
