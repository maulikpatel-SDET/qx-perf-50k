"""Service module 36595: business logic, no crypto."""


def calculate_total_36595(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36595():
    return 'module 36595 handles orders and invoices'
